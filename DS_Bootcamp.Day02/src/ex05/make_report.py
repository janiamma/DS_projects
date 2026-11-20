import sys
from analytics import Research
from analytics import Analytics
import config

def main():
    try:
        if len(sys.argv) != 2:
            print("Usage: python3 make_report.py ../ex00/data.csv")
            sys.exit(1)

        file_path = sys.argv[1]
        research_object = Research(file_path)
        data = research_object.file_reader()
        if isinstance(data, str):
            print(data)
            sys.exit(1)

        calculations = Analytics(data)    # создаём новый объект
        counts = calculations.counts()    # применяем метод из класса Analytics и сохраняем в переменную
        fractions = calculations.fractions()
        random_predictions = calculations.predict_random(config.num_of_steps)  # применяем метод с вызовом переменной из config

        # Формируем отчет
        total_observations = sum(counts) # сумма списков в списке 'counts'
        heads, tails = counts    # распаковываем списки из 'counts'
        tail_fraction = fractions[1]  # второй элемент списка 'fractions'
        head_fraction = fractions[0]  # первый элемент списка 'fractions'
        forecast_heads = random_predictions.count([1, 0])
        forecast_tails = random_predictions.count([0, 1])

        report = config.report_template.format(     # присваиваем переменные для использования в шаблоне 'report'
            total=total_observations,
            tails=tails,
            heads=heads,
            tail_fraction=tail_fraction,
            head_fraction=head_fraction,
            forecast_steps=config.num_of_steps,
            predict_tails=forecast_tails,
            predict_heads=forecast_heads
        )

        print(report)
        calculations.save_file(report, "heads_tails_report", "txt")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
