import main

def run_test():
    try:
        main.main()
        print("Test Run main.py successful")
    except Exception as e:
        print(f"Test failed: {str(e)}")

if __name__ == "__test__":
    run_test()
