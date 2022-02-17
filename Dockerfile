FROM ubuntu

# Ubuntu Dependencies
RUN apt-get update && apt-get install -y \
    python3-pip


# Copy HOST backend to CONTAINER /opt/wordle_tool_app 
WORKDIR /opt/wordle_tool_app
COPY ./backend .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
