import os
import sys
import argparse

import cv2
import torch

sys.path.insert(0, os.path.abspath('.'))

from flexinfer.tasks import build_segmentor
from flexinfer.preprocess import transforms as TF
from flexinfer.postprocess import postprocess as PP
from flexinfer.utils import set_device


def main(imgfp):
    gpu_id = 0
    # 1. set gpu id, default gpu id is 0
    set_device(gpu_id=gpu_id)
    use_gpu = torch.cuda.is_available()

    # 2. prepare for transfoms and model
    ## 2.1 transforms
    transform = TF.Compose([
        TF.PadIfNeeded(513, 513),
        TF.ToTensor(use_gpu=use_gpu),
        TF.Normalize(use_gpu=use_gpu),
    ])
    batchify = TF.Batchify(transform)

    ## 2.2 postprocess
    postprocess = PP.Compose([
        ### for single-label mode
        PP.SoftmaxProcess(),
        ### for multi-label model
        # PP.SigmoidProcess(threshold=0.5),
        PP.InversePad()
    ])

    ## 2.3 model
    ### build segmentor with trt engine from onnx model
    segmentor = build_segmentor(build_from='onnx',
                                model='checkpoint/voc_deeplabv3.onnx',
                                max_batch_size=2, fp16_mode=True)
    ### build segmentor with trt engine from serialized engine
    # segmentor = build_segmentor(build_from='engine',
    #                             engine='voc_deeplabv3.engine')

    # 3. load image
    img = cv2.imread(imgfp)

    imgs = [img, img]
    shape_list = [img.shape[:2] for img in imgs]

    # 4. inference
    tensor = batchify(imgs)
    outp = segmentor(tensor)
    outp = postprocess(outp, **dict(shape_list=shape_list))

    print(outp)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Segmentor demo')
    parser.add_argument('imgfp', type=str, help='path to image file path')
    args = parser.parse_args()
    main(args.imgfp)
