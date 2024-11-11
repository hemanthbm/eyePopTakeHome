import unittest
import asyncio
from unittest.mock import patch, MagicMock
from eyepop_processor.processor import process_image

class TestProcessor(unittest.TestCase):

    @patch('eyepop_processor.processor.EyePopSdk')
    def test_process_image_success(self, MockSdk):
        # Mock the endpoint and its methods
        mock_endpoint = MagicMock()
        MockSdk.endpoint.return_value = mock_endpoint

        # Mock upload and predict responses
        mock_job = MagicMock()
        mock_job.predict.return_value = {
            'objects': [
                {
                    'category': 'common-objects',
                    'classId': 1,
                    'classLabel': 'person',
                    'confidence': 0.967,
                    'height': 196.999,
                    'id': 1,
                    'orientation': 0,
                    'width': 105.726,
                    'x': 251.417,
                    'y': 280.737
                }
            ],
            'system_timestamp': 1731292953334990000
        }
        mock_endpoint.upload.return_value = mock_job

        # Run the function with a mock file path
        result = asyncio.run(process_image("/path/to/mock_image.jpg"))
        
        # Assert the results
        self.assertIn('objects', result)
        self.assertEqual(result['objects'][0]['classLabel'], 'person')
        self.assertEqual(result['objects'][0]['confidence'], 0.967)

    @patch('eyepop_processor.processor.EyePopSdk')
    def test_process_image_error(self, MockSdk):
        # Mock the endpoint with an error on upload
        mock_endpoint = MagicMock()
        MockSdk.endpoint.return_value = mock_endpoint

        # Simulate an error during the upload process
        mock_endpoint.upload.side_effect = Exception("Upload failed")

        # Run the function with a mock file path
        result = asyncio.run(process_image("/path/to/mock_image.jpg"))

        # Assert the error handling
        self.assertIn('error', result)
        self.assertEqual(result['error'], "Upload failed")

if __name__ == "__main__":
    unittest.main()
