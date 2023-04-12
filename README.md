# Modile test

Modile тест включает в себя два теста на проверку поиска данных на сайте wikipedia.org, написанных с помощью облачной платформы для 
мобильного тестирования - Browserstack

## <img width="30px" title="Jenkins" src="https://user-images.githubusercontent.com/118905261/230335250-74a96dcc-6029-423c-9faf-f4551b7a9448.png"> Запуск проекта в Jenkins

[Ссылка на сборку](https://jenkins.autotests.cloud/job/qa_guru_python_3_20_jenkins/)

При нажатии на "Собрать сейчас" начнется сборка тестов и их прохождение, через виртуальную машину в Selenide.

<img width="1728" alt="Снимок экрана 2023-04-06 в 12 40 54" src="https://user-images.githubusercontent.com/118905261/230445564-7854e5cc-60a5-4ab7-a0a5-4bc4dfc8de3b.png">

После сборки тестов формируется Allure отчет. Открыть его можно нажав на иконку  <img width="10px" title="Allure Report" src="https://user-images.githubusercontent.com/118905261/230338875-2f21268b-e367-4705-b7a8-a5a9ef1698d2.png">

<img width="1728" alt="Снимок экрана 2023-04-06 в 12 41 10" src="https://user-images.githubusercontent.com/118905261/230445587-f4bc9df5-c811-4bdd-b777-3362eea8620f.png">

## <img width="30px" title="Allure Report" src="https://user-images.githubusercontent.com/118905261/230338875-2f21268b-e367-4705-b7a8-a5a9ef1698d2.png"> Allure отчет

Вкладка "Overview" включает в себя отчет по тесту, дату прохождения теста и затраченное время на прохождение теста

<img width="1728" alt="Снимок экрана 2023-04-06 в 12 45 27" src="https://user-images.githubusercontent.com/118905261/230445935-829f47ac-755c-4c57-a8e1-63a9c6ff8bf5.png">

<img width="1728" alt="Снимок экрана 2023-04-06 в 19 58 11" src="">

На вкладке "Suites" можно найти подробную информацию о тесте: предусловия, шаги теста и вложения (скриншот, видео и логи)

<img width="1728" alt="Снимок экрана 2023-04-06 в 12 45 45" src="https://user-images.githubusercontent.com/118905261/230445967-d152c20e-f655-4b6e-a5cc-ce7d4e159471.png">
