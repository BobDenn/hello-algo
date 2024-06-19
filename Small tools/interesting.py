import pyscreenshot as ImageGrab
import pytesseract
import pyautogui
import pyperclip
import time


pytesseract.pytesseract.tesseract_cmd = r'C:\Tesseract-OCR\tesseract.exe'

def capture_screen(region=None):
    """
    捕获屏幕截图。
    
    :param region: 截图区域 (left_x, top_y, right_x, bottom_y)，如果为 None, 则捕获全屏。
    :return: 截图图像
    """
    if region:
        screenshot = ImageGrab.grab(bbox=region)
    else:
        screenshot = ImageGrab.grab()
    return screenshot

def extract_text_from_image(image):
    """
    从图像中提取文字。
    :param image: 输入图像
    :return: 提取的文字
    """
    text = pytesseract.image_to_string(image, lang='chi_sim')
    return text

def check_text(content):
    """
    检查文本内容是否包含关键字或短语。
    
    :param content: 输入文本
    :return: 检查结果
    """
    keywords = ["华为", "润", "就业", "物价低", "Huawei", "经济环境", "变差"]
    for keyword in keywords:
        if keyword in content:
            return "加油华为! 加油China!"
    return " "

def paste_text_from_clipboard(message):
    """
    将文本从剪贴板粘贴到当前焦点位置。
    :param message: 要粘贴的消息
    """
    pyperclip.copy(message)
    pyautogui.hotkey('ctrl', 'v')  # 触发粘贴操作

def type_and_send_message(message, input_box_coords, send_button_coords):
    """
    在QQ聊天窗口中输入并发送消息。
    :param message: 要发送的消息
    :param input_box_coords: 输入框的坐标 (x, y)
    :param send_button_coords: 发送按钮的坐标 (x, y)
    """
    # 点击输入框
    pyautogui.click(input_box_coords)
    time.sleep(0.5)
    # 输入消息
    print("开始输入")
     # 使用粘贴方式输入消息
    paste_text_from_clipboard(message)
    print("输入完毕")
    # 点击发送按钮
    pyautogui.click(send_button_coords)

if __name__ == "__main__":
    # 定义截图区域
    region = (12, 84, 752, 656)

    # 捕获屏幕截图
    screenshot = capture_screen(region)

    # 从截图中提取文字
    text = extract_text_from_image(screenshot)

    # 检查提取的文字内容
    result = check_text(text)

    # 短暂延时，确保QQ聊天窗口为当前活动窗口
    time.sleep(2)  # 2秒延时，可以根据实际情况调整

    # 定义输入框和发送按钮的坐标 
    input_box = (30, 750)  
    
    send_button = (881, 884)  
    # 自动输入并发送消息
    type_and_send_message(result, input_box, send_button)
    
