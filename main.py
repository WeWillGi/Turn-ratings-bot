def add_numbers(a, b):
    return a + b
  
def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(0, 0) == 0
    assert add_numbers(-1, 1) == 0
    
def main():
  print("hello world")


if __name__ == "__main__":
    main()
