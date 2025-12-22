#include <iostream>
#include "Functions.h"

using namespace std;

int main() {
	setlocale(LC_ALL, "Russian");
	double x, y;

	cout << "Введите значение X: ";
	cin >> x;
	cout << "Введите значение Y: ";
	cin >> y;

	double R, S, C;

	try {
		solve(x, y, R, S, C);

		cout << "\nРезультаты вычислений:" << endl;
		cout << "R = " << R << endl;
		cout << "S = " << S << endl;
		cout << "Максимальное значение C = " << C << endl;
	}
	catch (const exception& e) {
		cout << "Ошибка: " << e.what() << endl;
	}

	system("pause");
	return 0;
}