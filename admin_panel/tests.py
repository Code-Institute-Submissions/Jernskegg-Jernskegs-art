from django.test import TestCase

from .views import check_file_format
# Create your tests here.


class testFileChecking(TestCase):
    '''
    Test if  check_files_form with input of request.FILES
    in views has the correct files
    '''

    def test_file_check_png(self):

        case_png = "<MultiValueDict: {'image': [<InMemoryUploadedFile: \
        generatedworld.png (image/png)>], 'water_marked_image': \
        [<InMemoryUploadedFile: generatedworld.png (image/png)>]}>"

        self.assertTrue(check_file_format(case_png))

    def test_file_check_jpeg(self):

        case_jpeg = "<MultiValueDict: {'image': [<InMemoryUploadedFile: \
        krita.jpg (image/jpeg)>], 'water_marked_image': \
        [<InMemoryUploadedFile: krita.jpg (image/jpeg)>]}>"

        self.assertTrue(check_file_format(case_jpeg))

    def test_file_check_wrong(self):

        case_wrong = "<MultiValueDict: {'image': [<TemporaryUploadedFile: \
        Certificate_part.stl (application/octet-stream)>], \
        'water_marked_image': \
        [<TemporaryUploadedFile: Certificate_part.stl \
        (application/octet-stream)>]}>"

        self.assertFalse(check_file_format(case_wrong))

    def test_file_check_one_correct_one_wrong(self):

        case_weird = "<MultiValueDict: {'image': [<InMemoryUploadedFile: \
        krita.jpg (image/jpeg)>], 'water_marked_image': \
        [<TemporaryUploadedFile: Certificate_part.stl \
        (application/octet-stream)>]}>"

        self.assertFalse(check_file_format(case_weird))

    def test_file_check_empty(self):
        self.assertFalse(check_file_format())
