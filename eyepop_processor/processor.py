import os
from eyepop import EyePopSdk

async def process_image(image_path: str):
    """
    Process a local image file by uploading it to the EyePop.ai API.

    Args:
        image_path (str): The path to the local image file.

    Returns:
        dict: Parsed response from the EyePop.ai API.
    """
    endpoint = EyePopSdk.endpoint(
        # Add your EYEPOP_POP_ID and EYEPOP_SECRET_KEY as environment variables
        pop_id=os.environ.get('EYEPOP_POP_ID'),
        secret_key=os.environ.get('EYEPOP_SECRET_KEY'),
    )

    endpoint.connect()
    try:
        result = endpoint.upload(image_path).predict()
        return result
    except Exception as e:
        print(f"Error processing image: {e}")
        return {"error": str(e)}
    finally:
        endpoint.disconnect()
