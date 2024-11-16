import csv


def parse_log_file(log_file_path):
    safe_counts = []
    safe_count = 0
    interval = 500
    current_count = 0

    with open(log_file_path, 'r', encoding='utf-8') as file:
        for line in file:
            if '[TRACE] Validating' in line and line.strip().endswith('.fuzz ...'):
                current_count += 1
                if current_count % interval == 0:
                    safe_counts.append((current_count, safe_count))
                    safe_count = 0  # Reset safe count for the next interval
            
            if '[VERBOSE]' in line and 'is safe' in line:
                safe_count += 1

            

    # If there are any remaining files that didn't make up a complete interval
    if current_count % interval != 0:
        safe_counts.append((current_count, safe_count))

    return safe_counts

def write_csv(output_file_path, data):
    with open(output_file_path, 'w', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['Interval', 'Safe Count'])
        csvwriter.writerows(data)

if __name__ == "__main__":
    file_path = '../outputs/full_run/deepseek-coder/'  # 修改为日志文件的路径

    log_file_path = file_path + "log_validation.txt"
    output_file_path = file_path + 'safe_counts.csv'

    safe_counts = parse_log_file(log_file_path)
    write_csv(output_file_path, safe_counts)

    print(f'Safe counts have been written to {output_file_path}')
