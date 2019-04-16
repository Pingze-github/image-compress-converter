import os
from PIL import Image
from shutil import copyfile

class Mode():
  Advanced = 1
  Compatible = 2
  AdvancedWithCompatible = 3

class Quality():
  Best = 95
  Appropriate = 75
  Low = 50

class ConverterOptions:
  def __init__(self, mode=Mode.AdvancedWithCompatible, quality=Quality.Best):
    self.mode = mode
    self.quality = quality

class Converter:
  def __init__(self, opts):
    self.opts = opts

  def repaint_dir(self, in_dir_path, out_dir_path):
    if not os.path.isdir(out_dir_path):
      os.mkdir(out_dir_path)
    for path, dir_list, file_list in os.walk(in_dir_path):
      relative_path = path.lstrip(in_dir_path + os.sep)
      for file_name in file_list:
          file_path = os.path.join(path, file_name)
          file_out_path = self.__create_out_path(out_dir_path, relative_path, file_name)
          in_path, out_path = self.repaint_file(file_path, file_out_path)
          self.log(in_path, out_path)

  def log(self, in_path, out_path):
          in_path_size = os.path.getsize(in_path)
          out_path_size = os.path.getsize(out_path)
          compress_rate = out_path_size / in_path_size
          print('{} ({}) => {} ({}) - {:.2f}%'.format(in_path, fsize(in_path_size),
                                                      out_path, fsize(out_path_size), compress_rate * 100))
  
  def repaint_file(self, in_path, out_path):
    out_dir_path = os.path.dirname(out_path)
    if not os.path.isdir(out_dir_path):
      os.mkdir(out_dir_path)

    with Image.open(in_path) as im:
      # remove image info
      im.info = {}

      if self.opts.mode == Mode.Advanced:
        out_path += '.webp'
        im.save(out_path, format='webp',
                quality=self.opts.quality, save_all=True)

      elif self.opts.mode == Mode.Compatible:
        if im.format == 'GIF':
          out_path += '.gif'
          copyfile(in_path, out_path)
        elif im.mode == 'RGBA':
          out_path += '.jpg'
          im.save(out_path, optimize=True, format='png')
        else:
          out_path += '.jpg'
          im.save(out_path, quality=self.opts.quality, format='jpeg')

      elif self.opts.mode == Mode.AdvancedWithCompatible:
        if im.format == 'GIF':
          out_path += '.gif'
          copyfile(in_path, out_path)
        else:
          out_path += '.jpg'
          im.save(out_path, format='webp', quality=self.opts.quality)

      else:
        raise Exception('No valid mode selected')
    
    return in_path, out_path

  def __create_out_path(self, out_dir_path, relative_path, file_name):
    portion = os.path.splitext(file_name)
    file_name = portion[0]
    return os.path.join(out_dir_path, relative_path, file_name)


def fsize(size):
  kb = 1024
  mb = kb*1024
  gb = mb*1024
  tb = gb*1024
  if size >= tb:
    return "%.1f TB" % float(size / tb)
  if size >= gb:
    return "%.1f GB" % float(size / gb)
  if size >= mb:
    return "%.1f MB" % float(size / mb)
  if size >= kb:
    return "%.1f KB" % float(size / kb)

def test():
  c = Converter(ConverterOptions())
  c.repaint_dir('./test/原始', './test/输出')

if __name__ == '__main__':
  test()
