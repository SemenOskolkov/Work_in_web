import json
from http.server import BaseHTTPRequestHandler, HTTPServer

hostName = 'localhost'
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):

    def do_GET(self):  # Функция по обработке GET запросов
        result_string = "Hello, World wide web!"
        # data_from_list = []

        # data_from_list.append(result_string, "utf-8")

        self.send_response(200)  # Формируем ответ с кодом
        self.send_header("Content-type", "application/text")  # Получение заголовка
        self.end_headers()  # Заголовки записаны
        self.wfile.write(bytes(result_string, "utf-8"))  # Запись результата ответа к клиенту

    def do_POST(self): # Функция по обработке POST запросов
        data_from_list = []  # Выбираем данные

        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)  # Чтение тела запроса

        data_from_request = post_data  #
        data_from_list.append(data_from_request, "utf-8")  # Добавление информации на запись

        self.send_response(201)  # Формируем ответ с кодом
        self.send_header("Content-type", "application/text")  # Получение заголовка
        self.end_headers()  # Заголовки записаны
        self.wfile.write(bytes('{"result":"ok"}', "utf-8"))  # Отправление результата ответа


if __name__ == "__main__":
    webserver = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s;%s" % (hostName, serverPort))
    try:
        webserver.serve_forever()
    except KeyboardInterrupt:
        pass
    webserver.server_close()
    print("Server stopped.")