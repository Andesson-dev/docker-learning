FROM ubuntu:latest

RUN apt update && apt install -y stress

CMD ["stress", "--cpu", "1", "--timeout", "60"]