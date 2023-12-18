from random import randint as rd


class Router:
    servers = {}
    buffer = tuple()

    @classmethod
    def link(cls, server):
        cls.servers[server.ip] = server

    @classmethod
    def unlink(cls, server):
        cls.servers.pop(server.ip, None)
        Server.ip_addresses.discard(server.ip)

    @classmethod
    def send_data(cls):
        for data in cls.buffer:
            check_data = cls.servers.get(data.ip)
            if check_data is not None:
                check_data.buffer.append(data)

        cls.buffer = tuple()


class Server:
    ip_addresses = set()

    def __init__(self):
        self.buffer = []
        self.ip = self.create_ip()

    @classmethod
    def create_ip(cls):
        length, ip = len(cls.ip_addresses), ""
        while length == len(cls.ip_addresses):
            ip = cls.ip_generation()
            cls.ip_addresses.add(ip)

        return ip

    @staticmethod
    def ip_generation():
        ip = (f"{rd(1, 9)}{rd(1, 9)}{rd(1, 9)}" for _ in range(4))
        return ".".join(ip)

    @staticmethod
    def send_data(data):
        Router.buffer += (data,)

    def get_data(self):
        data = self.buffer.copy()
        self.buffer.clear()
        return data

    def get_ip(self):
        return self.ip


class Data:

    def __init__(self, data, ip):
        self.data = data
        self.ip = ip
