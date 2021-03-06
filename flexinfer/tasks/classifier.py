import torch
from volksdep.converters import onnx2trt, load

from .base_task import BaseTask


class TRTClassifier(BaseTask):
    def __init__(self, build_from, *args, **kwargs):
        if build_from == 'onnx':
            func = onnx2trt
        elif build_from == 'engine':
            func = load
        else:
            raise ValueError('Unsupported build_from value %s, valid build_from value is torch, onnx and engine' % build_from)
        model = func(*args, **kwargs)
        super().__init__(model)

    def __call__(self, imgs):
        """
        Args:
            imgs (torch.float32): shape N*3*H*W

        Returns:
            feats (np.float32): shape N*K, K is the number of classes
        """
        with torch.no_grad():
            imgs = imgs.cuda()
            outp = self.model(imgs)
            outp = outp.cpu()
        outp = outp.numpy()

        return outp


def build_classifier(*args, **kwargs):
    return TRTClassifier(*args, **kwargs)
