import asyncio
import argparse
from eyepop_processor.processor import process_image

async def main(image_path):
    #image_path = "./test.jpg"
    result = await process_image(image_path)
    print(result)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process an image using EyePop.ai API.")
    parser.add_argument("image_path", type=str, help="Path to the local image file")
    args = parser.parse_args()

    asyncio.run(main(args.image_path))