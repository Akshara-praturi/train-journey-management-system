import sys

distance = {
    "CHN": 0, "SLM": 350, "BLR": 550, "KRN": 900, "HYB": 1200,
    "NGP": 1600, "ITJ": 1900, "BPL": 2000, "AGA": 2500, "NDL": 2700,
    "TVC": 0, "SRR": 300, "MAQ": 600, "MAO": 1000, "PNE": 1400,
    "PTA": 3800, "NJP": 4200, "GHY": 4700
}

def filter_bogies(bogies):
    result = []
    found_hyb = False

    for b in bogies:
        if b == "HYB":
            found_hyb = True
            continue
        if found_hyb:
            result.append(b)

    return result

def main():
    lines = sys.stdin.readlines()

    train_a = []
    train_b = []

    for line in lines:
        parts = line.strip().split()
        if parts[0] == "TRAIN_A":
            train_a = parts[2:]
        elif parts[0] == "TRAIN_B":
            train_b = parts[2:]

    a_filtered = filter_bogies(train_a)
    b_filtered = filter_bogies(train_b)

    print("ARRIVAL TRAIN_A ENGINE", *a_filtered)
    print("ARRIVAL TRAIN_B ENGINE", *b_filtered)

    merged = a_filtered + b_filtered

    if not merged:
        print("JOURNEY_ENDED")
        return

    merged.sort(key=lambda x: distance[x], reverse=True)

    print("DEPARTURE TRAIN_AB ENGINE ENGINE", *merged)

if __name__ == "__main__":
    main()