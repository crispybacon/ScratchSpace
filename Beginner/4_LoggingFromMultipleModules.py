import logging
import mylib

def main():
    logging.basicConfig(filename='myapp.log', level=logging.INFO)
    logging.info('Started')
    logging.info(mylib.do_something())
    logging.info('Finished')

if __name__ == '__main__':
    main()