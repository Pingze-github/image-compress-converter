import os
from PIL import Image
from shutil import copyfile

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

def repaint_file(in_path, out_path):
  out_dir_path = os.path.dirname(out_path)
  if not os.path.isdir(out_dir_path):
    os.mkdir(out_dir_path)

  im = Image.open(in_path)
  # remove image info
  im.info = {};
  if im.format == 'GIF':
    out_path += '.gif'
    # im.save(out_path + '.gif', format='webp', save_all=True)
    copyfile(in_path, out_path)
  else:
    out_path += '.jpg'
    im.save(out_path, format='webp', quality=95)
  im.close()
  return in_path, out_path

def create_out_path(out_dir_path, relative_path, file_name):
  portion = os.path.splitext(file_name)
  file_name = portion[0]
  return os.path.join(out_dir_path, relative_path, file_name)

def repaint_dir(in_dir_path, out_dir_path):
  if not os.path.isdir(out_dir_path):
    os.mkdir(out_dir_path)
  for path, dir_list, file_list in os.walk(in_dir_path):
    relative_path = path.lstrip(in_dir_path + os.sep)
    for file_name in file_list:  
        file_path = os.path.join(path, file_name)
        file_out_path = create_out_path(out_dir_path, relative_path, file_name)
        in_path, out_path = repaint_file(file_path, file_out_path)

        in_path_size = os.path.getsize(in_path)
        out_path_size = os.path.getsize(out_path)
        compress_rate = out_path_size / in_path_size
        print('{} ({}) => {} ({}) - {:.2f}%'.format(in_path, fsize(in_path_size),
                                                    out_path, fsize(out_path_size), compress_rate * 100))

def main():
  repaint_dir('./test/原始', './test/输出')

  # repaint_file('./test/原始/501.jpg', './test/输出/501.jpg')


if __name__ == '__main__':
  main()
