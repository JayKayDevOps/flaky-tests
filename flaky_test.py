import random
import time
import pandas as pd
import matplotlib.pyplot as plt

RESULTS_FILE = "test_results.csv"

def simulate_flaky_test() -> bool:
    """
    Simulates a flaky test with a 20% chance of failure.
    """
    return random.random() > 0.01  # 80% pass, 20% fail

def run_tests(iterations: int = 10):
    """
    Runs the flaky test multiple times and stores results.
    """
    results = []

    for i in range(iterations):
        passed = simulate_flaky_test()
        results.append({"run": i + 1, "status": "PASS" if passed else "FAIL"})
        print(f"Run {i+1}: {'PASS' if passed else 'FAIL'}")
        time.sleep(0.1)  # Simulate real test execution time

    df = pd.DataFrame(results)
    df.to_csv(RESULTS_FILE, index=False)
    print(f"Results saved to {RESULTS_FILE}")

def generate_graph():
    """
    Generates a bar chart of test results.
    """
    df = pd.read_csv(RESULTS_FILE)
    pass_count = len(df[df["status"] == "PASS"])
    fail_count = len(df[df["status"] == "FAIL"])

    plt.bar(["PASS", "FAIL"], [pass_count, fail_count], color=["green", "red"])
    plt.xlabel("Test Result")
    plt.ylabel("Count")
    plt.title("Flaky Test Simulation Results")
    plt.savefig("test_results.png")
    print("Graph saved as test_results.png")

def generate_report():
    """
    Generates an HTML report summarizing the test results.
    """
    df = pd.read_csv(RESULTS_FILE)
    pass_rate = (df["status"] == "PASS").mean() * 100
    fail_rate = 100 - pass_rate

    report_html = f"""
    <html>
    <head><title>Flaky Test Report</title></head>
    <body>
        <h1>Flaky Test Report</h1>
        <p>Total Runs: {len(df)}</p>
        <p>Pass Rate: {pass_rate:.2f}%</p>
        <p>Fail Rate: {fail_rate:.2f}%</p>
        <img src="test_results.png" alt="Test Results Graph">
    </body>
    </html>
    """

    with open("test_report.html", "w") as f:
        f.write(report_html)
    print("Report saved as test_report.html")

if __name__ == "__main__":
    run_tests()
    generate_graph()
    generate_report()
