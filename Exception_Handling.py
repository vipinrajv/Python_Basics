try:
    n=int(input("Enter a number "))
    r=1/n

except ZeroDivisionError:
    print("you cann't divide by zero ")
except ValueError:
    print("Enter numbers only ")
except Exception:
    print("Something went wrong ")
else:
    print(f"Result = {r}")
finally:
    print("Execution completed")