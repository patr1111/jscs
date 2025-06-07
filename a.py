from PIL import Image, ImageDraw, ImageFont

# 入力テキストファイルのパス
input_text_path = "input.txt"
# 出力画像ファイルのパス
output_image_path = "output.png"

# テキストファイルの内容を読み込む
with open(input_text_path, "r", encoding="utf-8") as file:
    text = file.read()

# 画像のサイズと背景色を設定
image_width = 800
image_height = 600
background_color = (255, 255, 255)  # 白

# 画像を作成
image = Image.new("RGB", (image_width, image_height), background_color)
draw = ImageDraw.Draw(image)

# フォントを設定
font = ImageFont.load_default()

# テキストを画像に描画
text_color = (0, 0, 0)  # 黒
margin = 10
offset = margin
for line in text.split("\n"):
    draw.text((margin, offset), line, font=font, fill=text_color)
    offset += draw.textbbox((0, 0), line, font=font)[3] + margin

# 画像を保存
image.save(output_image_path)

print(f"テキストが画像に変換されました。結果は {output_image_path} に保存されました。")
