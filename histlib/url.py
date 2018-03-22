from yahoo_finance import Share


def main():
	com = Share("MSFT");
	print com.get_open();

if __name__ == '__main__':
    main()