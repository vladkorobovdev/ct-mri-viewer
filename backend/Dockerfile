FROM eclipse-temurin:25-jdk

WORKDIR /app

COPY gradlew .
COPY gradle gradle
COPY build.gradle* settings.gradle* ./

RUN chmod +x gradlew && ./gradlew dependencies --no-daemon

COPY src src

EXPOSE 8080 5005

CMD ["sh", "-c", "./gradlew classes processResources --continuous & ./gradlew bootRun"]

