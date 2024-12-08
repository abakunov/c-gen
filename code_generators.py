import treepoem
from PIL import Image


def generate_EAN13(encoding) -> Image.Image:
    image = treepoem.generate_barcode(
        barcode_type="ean13",
        data=str(encoding),
    )
    return image


def generate_QR(encoding) -> Image.Image:
    image = treepoem.generate_barcode(
        barcode_type="qrcode",
        data=str(encoding),
    )
    return image


def generate_DataMatrix(encoding) -> Image.Image:
    image = treepoem.generate_barcode(
        barcode_type="datamatrix",
        data=str(encoding),
    )
    return image
