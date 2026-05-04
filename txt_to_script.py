import json
import os
import re

input_file = "script_input.txt"
output_file = "script_output.json"

# 默认设置参数
DEFAULT_SPEAKER = "PERFORMER"
DEFAULT_TYPE = "self"  # 或者 "ai"
DEFAULT_VOICE = "yes"  # 或者 "no"

if not os.path.exists(input_file):
    with open(input_file, "w", encoding="utf-8") as f:
        f.write("这是第一段台词。\n\n这是第二段台词，比较长，所以停顿时间系统会自动计算得更久一些。\n\n第三段台词结束。")
    print(f"已自动创建示例输入文件 {input_file}，请放入文段后重新运行。")
else:
    segments = []
    with open(input_file, "r", encoding="utf-8") as f:
        content = f.read().strip()
        
        # 1. 统一替换不同操作系统的换行符，将 Windows 的 \r\n 变为标准的 \n
        content = content.replace("\r\n", "\n").replace("\r", "\n")
        
        # 2. 智能切分段落
        if "\n\n" in content:
            # 如果文本中存在空行（两个以上的连续换行），则按空行切分
            paragraphs = [p.strip() for p in re.split(r'\n{2,}', content) if p.strip()]
        else:
            # 如果文本中没有任何空行，则按单行切分
            paragraphs = [p.strip() for p in content.split("\n") if p.strip()]

        for p in paragraphs:
            # 自动估算时长：基础 2500 毫秒 + 每个字符 60 毫秒
            calculated_pause = 2500 + (len(p) * 60)
            
            segment = {
                "speaker": DEFAULT_SPEAKER,
                "type": DEFAULT_TYPE,
                "pause": calculated_pause,
                "voice": DEFAULT_VOICE,
                "text": p
            }
            segments.append(segment)

    output_data = { "segments": segments }

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2)

    print(f"成功将 {len(segments)} 段台词转换为 Script 格式并保存至 {output_file}！")