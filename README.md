# ms-img2vid Cog model

This is an implementation of the [fffilono/ms-image2video](https://huggingface.co/spaces/fffiloni/MS-Image2Video) (aka camenduru/damo-image-to-video) model as a Cog model. [Cog packages machine learning models as standard containers.](https://github.com/replicate/cog)

First, download the pre-trained weights:

    cog run script/download-weights

Then, you can run predictions:

    cog predict -i image=@demo.jpeg

## Example:

![alt text](boat.gif)
