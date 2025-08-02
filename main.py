class Image():
    def __init__(self, resolution='0x0', title='photo', extension='.'):
        self.resolution = resolution
        self.title = title
        self.extension = extension

    def resize(self, res):
        self.resolution = res

    def title_under(self):
        self.title = self.title.under()

    def title_upper(self):
        self.title = self.title.upper()


my_photo = Image(resolution='1280x900', extension='.png')
print(my_photo.extension, my_photo.title, my_photo.resolution)

my_photo.resize('100x100')
my_photo.title_under()
print(my_photo.extension, my_photo.title, my_photo.resolution)
