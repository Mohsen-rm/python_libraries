import cv2
import moviepy.editor as mp
from PIL import Image

def watermarkVideo(path_video,path_logo,out_video):
    video = mp.VideoFileClip(path_video)
    logo = (mp.ImageClip(path_logo)
            .set_duration(video.duration)
            .resize(height=25) # ارتفاع الشعار
            .margin(right=6, bottom=6, opacity=0) # (اختياري) هوامش حول الشعار
            .set_pos(("right","bottom"))) # وضع الشعار

    final = mp.CompositeVideoClip([video, logo])
    final.write_videofile(out_video)


def watermarkImage(input_image_path, output_image_path, watermark_image_path, distance):
    base_image = Image.open(input_image_path)
    watermark = Image.open(watermark_image_path)

    watermark = watermark.resize((56, 56))  # تغيير حجم العلامة المائية إلى 56x56

    width, height = base_image.size
    watermark_width, watermark_height = watermark.size

    # حساب الموقع للصق العلامة المائية مع المسافة
    paste_position = (width - watermark_width - distance, height - watermark_height - distance)

    # لصق العلامة المائية على الصورة الأساسية
    base_image.paste(watermark, paste_position, watermark)

    # حفظ النتيجة
    base_image.save(output_image_path)



input_image_path = "img.png"  # استبدل بمسار صورتك الأساسية
output_image_path = "output_image.jpg"  # استبدل بالمسار المطلوب للناتج
watermark_image_path = "icon.png"  # استبدل بمسار صورة العلامة المائية
distance_from_bottom_and_right = 6  # تعيين المسافة حسب الحاجة

watermarkImage(input_image_path, output_image_path, watermark_image_path, distance_from_bottom_and_right)
watermarkVideo("video4.mp4","icon.png","out_video2.mp4")
