#include <iostream> 
#include <cmath>

int main() {
	setlocale(LC_ALL, "Russian");
	double x, y;

	std::cout << "Введите значение X: ";
	std::cin >> x;
	std::cout << "Введите значение Y: ";
	std::cin >> y;

	double R = pow(fabs(sin(x) / y), 1.0 / 4.0);
	double S = log10(pow(2, y));

	double C = std::max(R, S);

	std::cout << "\nРезультаты вычислений:" << std::endl;
	std::cout << "R = " << R << std::endl;
	std::cout << "S = " << S << std::endl;
	std::cout << "Максимальное значение C = " << C << std::endl;
	
	system("pause");
	return 0;
}