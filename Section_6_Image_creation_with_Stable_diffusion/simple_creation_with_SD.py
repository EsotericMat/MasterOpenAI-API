import io
import os
from PIL import Image
import warnings
from stability_sdk import client
import stability_sdk.interfaces.gooseai.generation.generation_pb2 as generations
from dotenv import dotenv_values
from save_images import get_and_save_image
config = dotenv_values('../.env')
# Configure Open AI Key:
key = config['SD_KEY']

# Create Client
stab_api = client.StabilityInference(
    key=key,
    verbose=True
)


def generate_image_with_sd(prompt, seed=None, w=512, h=512, cfg_scale=None, n=1, sampler=generations.SAMPLER_K_DPMPP_2M):
    """
    :param prompt: Text to image
    :param seed: If given, will create the image over and over again with the same seed (Same results..)
    :param w: width of image
    :param h: height of image
    :param cfg_scale: how much it will stick to the prompt (default = 7.0)
    :param n: images
    :param sampler: which diffuser the model use.
    :return: content in binary
    """
    content = stab_api.generate(
        prompt=prompt,
        seed=seed,
        cfg_scale=cfg_scale,
        width=w,
        height=h,
        samples=n,
        sampler=sampler
    )
    for resp in content:
        for art in resp.artifacts:
            if art.finish_reason == generations.FILTER:
                warnings.warn('Safety Filtered')
                pass
            if art.type == generations.ARTIFACT_IMAGE:
                # img = Image.open(io.BytesIO(art.binary))
                return art.binary


if __name__ == '__main__':
    p = """3D art of monkey playing poker with humans sunglasses and smoke cigar"""
    img = generate_image_with_sd(prompt=p)
    get_and_save_image(img)
