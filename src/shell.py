from timeit import default_timer as timer
import volt

while True:
    text = input('volt >> ')
    if text == 'exit':
        break
    start = timer()
    volt.run(text)
    end = timer()
    print(f'Execution Completion => {end-start:.20f}')
    