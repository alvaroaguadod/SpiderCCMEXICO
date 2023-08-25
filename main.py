from scrapy.cmdline import execute
import os

# print(os.getcwd())
os.chdir("./CCMEXICO")


def to_scrapy_command(parameters: dict, spider_name: str):
    command = ["scrapy", "crawl", spider_name]
    for key, value in parameters.items():
        command.append("-a")
        command.append(f"{key}={value}")

    return command


parameters = dict(
    search='["gobierno"]',
    depth="3",
)


command = to_scrapy_command(parameters, spider_name="CCMEXICOSpider")
execute(argv=command + ["-o news.json"])
