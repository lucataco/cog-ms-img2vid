# Prediction interface for Cog

from cog import BasePredictor, Input, Path
from PIL import Image
from modelscope.pipelines import pipeline
from modelscope.outputs import OutputKeys

MODEL_NAME = 'damo/Image-to-Video'
MODEL_CACHE = 'model-cache'

class Predictor(BasePredictor):
    def setup(self) -> None:
        """Load the model into memory to make running multiple predictions efficient"""
        self.pipe = pipeline(
            task='image-to-video',
            model=MODEL_CACHE,
            model_revision='v1.1.0'
        )

    def predict(
        self,
        image: Path = Input(description="Input image"),
    ) -> Path:
        """Run a single prediction on the model"""
        pil_image = Image.open(image)
        output_video_path = self.pipe(
            pil_image,
            output_video='/tmp/output.mp4'
        )[OutputKeys.OUTPUT_VIDEO]

        return Path(output_video_path)
