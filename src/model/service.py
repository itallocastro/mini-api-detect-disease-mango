from fastapi import HTTPException, UploadFile
import PIL.Image as Image
import io
from keras.models import load_model
import numpy as np

model = load_model('./light_weight_model')


async def predict(file:  UploadFile):
    try:
        size_images = (224, 224)
        print(file.content_type)
        content_type = file.content_type
        if content_type not in ["image/jpeg", "image/png", "image/jpg", "image/*"]:
            raise HTTPException(status_code=400, detail="Invalid file type")
        image_bytes = await file.read()
        image = Image.open(io.BytesIO(image_bytes))
        image = image.resize(size_images)
        image = np.array(image)

        print(image.shape)

        predicted = model.predict(np.array([image]))
        print(predicted)

        await file.close()

        del image
        del image_bytes

        return {"result": predicted[0].tolist()}
    except Exception as e:
        print(e)
        raise e
