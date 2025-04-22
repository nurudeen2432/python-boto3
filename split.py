import os

def split_sql_file(input_file, output_dir, statements_per_file=5000):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    part = 1
    buffer = []
    statement_count = 0

    def write_part(part_number, statements):
        filename = os.path.join(output_dir, f'part_{part_number}.sql')
        with open(filename, 'w', encoding='utf-8') as f:
            f.writelines(statements)
        print(f"✅ Wrote: {filename} ({len(statements)} lines)")

    with open(input_file, 'r', encoding='utf-8', errors='ignore') as infile:
        for line in infile:
            buffer.append(line)
            if line.strip().endswith(';'):
                statement_count += 1

                if statement_count >= statements_per_file:
                    write_part(part, buffer)
                    buffer = []
                    part += 1
                    statement_count = 0

        # write remaining
        if buffer:
            write_part(part, buffer)

    print(f"\n✅ Done splitting into {part} file(s).")

# === USAGE ===
# Replace with your actual path
split_sql_file(r'C:\Users\nurudeen.durowade\Desktop\myexport6.txt.mssql', 'split_folder', statements_per_file=5000)
