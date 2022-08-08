import csv


def file_create(period, category_id, costs_list):

    with open(f'audit_app/static/data/{period}_{category_id}.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow((
            'N',
            'Costs',
            'Category',
            'Description',
            'Date'
        ))

    for n, cost in enumerate(costs_list, start=1):
        with open(f'audit_app/static/data/{period}_{category_id}.csv', 'a') as file:
            writer = csv.writer(file)
            writer.writerow((
                n,
                cost.count,
                cost.category.name,
                cost.description,
                cost.date_costs,
            ))

    return [f'audit_app/static/data/{period}_{category_id}.csv', f'data/{period}_{category_id}.csv']