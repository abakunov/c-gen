import os
import random
from PIL import Image, ImageDraw, ImageFilter, ImageOps
import treepoem
from code_generators import *
import numpy as np


def add_noise(image: Image.Image, amount: float = 0.02) -> Image.Image:
    """Adds random noise to the image."""
    np_image = np.array(image)
    noise = np.random.normal(0, 255 * amount, np_image.shape).astype(np.int32)
    noisy_image = np.clip(np_image + noise, 0, 255).astype(np.uint8)
    return Image.fromarray(noisy_image)


def add_dust(image: Image.Image, dust_count: int = 30) -> Image.Image:
    """Adds dust-like spots to the image."""
    draw = ImageDraw.Draw(image)
    for _ in range(dust_count):
        x, y = random.randint(0, image.width - 1), random.randint(0, image.height - 1)
        radius = random.randint(1, 3)
        draw.ellipse((x - radius, y - radius, x + radius, y + radius), fill="black")
    return image


def add_blur(image: Image.Image, radius: float = 2.0) -> Image.Image:
    """Applies Gaussian blur to the image."""
    return image.filter(ImageFilter.GaussianBlur(radius))


def add_rotation(image: Image.Image, angle: float = 5.0) -> Image.Image:
    """Applies a small rotation to the image."""
    return image.rotate(angle, resample=Image.BICUBIC, expand=True, fillcolor="white")


def add_contrast(image: Image.Image, factor: float = 0.8) -> Image.Image:
    """Adjusts the contrast of the image."""
    enhancer = ImageOps.autocontrast(image, cutoff=factor * 100)
    return enhancer


def apply_random_effects(image: Image.Image) -> Image.Image:
    """Applies random effects to the image."""
    effects = [
        lambda img: add_noise(img, amount=random.uniform(0.01, 0.05)),
        lambda img: add_dust(img, dust_count=random.randint(10, 20)),
        lambda img: add_blur(img, radius=random.uniform(1.0, 2.0)),
        lambda img: add_rotation(img, angle=random.uniform(-10, 10)),
        lambda img: add_contrast(img, factor=random.uniform(0.6, 1.2)),
    ]
    random.shuffle(effects)
    for effect in effects[:random.randint(1, len(effects))]:
        image = effect(image)
    return image
