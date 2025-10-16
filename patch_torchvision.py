# patch_disable_v2.py
import torchvision.transforms.v2 as T2
from torchvision.transforms.v2 import _transform

print("[patch_disable_v2] Patching torchvision.transforms.v2.Transform to bypass NotImplementedError")

def safe_transform(self, inpt, params=None):
    try:
        return self._transform(inpt, params)  
    except AttributeError:
        return inpt
    except NotImplementedError:
        return inpt

_transform.Transform.transform = safe_transform
