import json
import os

input_file = "log_input.txt"
output_file = "log_output.json"

if not os.path.exists(input_file):
    # 如果没有找到输入文件，自动创建一个空的示例文件
    with open(input_file, "w", encoding="utf-8") as f:
        f.write("06:00 system running...\n\n06:01 waiting for command...\n\n06:02 process completed.")
    print(f"已自动创建示例输入文件 {input_file}，请将你需要转化的 Log 每行/每段放进去后重新运行此脚本。")
else:
    with open(input_file, "r", encoding="utf-8") as f:
        content = f.read().strip()
        # 以换行或双换行切割，清理掉空白项
        lines = [line.strip() for line in content.split("\n") if line.strip()]

    output_data = { "logs": lines }

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2)

    print(f"成功将 {len(lines)} 条 Log 保存至 {output_file}！")