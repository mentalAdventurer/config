#include <iostream>
#include <string>

int main(int argc, char* argv[]) {
    std::string status_output;
    if (argc > 1) {
        status_output = argv[1];
    }
    char first_letter = status_output[0];
    std::string icon, text, class_, alt = "Time left", tooltip = "Time left", percentage = "100";

    if (first_letter == '?') {
        text = "";
    } else if (first_letter == 'R') {
        icon = "";
        text = icon + status_output.substr(1);
        class_ = "active";
    } else if (first_letter == 'P') {
        icon = "";
        text = icon + status_output.substr(1);
        class_ = "inactive";
    }

    std::cout << "{\"text\": \"" << text << "\", \"alt\": \"" << alt << "\", \"tooltip\": \"" << tooltip << "\", \"class\": \"" << class_ << "\", \"percentage\": " << percentage << " }" << std::endl;
    return 0;
}
