import time
from multiprocessing import Pool


def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line.strip())
    return all_data


filenames = [f'./file {number}.txt' for number in range(1, 5)]

if __name__ == "__main__":
    start_time = time.time()
    for filename in filenames:
        data = read_info(filename)
    print(f"{time.strftime('%H:%M:%S', time.gmtime(time.time() - start_time))} (линейный)")

    start_time = time.time()
    with Pool() as pool:
        results = pool.map(read_info, filenames)
    print(f"{time.strftime('%H:%M:%S', time.gmtime(time.time() - start_time))} (многопроцессный)")
