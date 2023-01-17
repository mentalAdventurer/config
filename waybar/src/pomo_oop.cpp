#include <iostream>
#include <string>

class Status {
private:
    std::string status_output_;

public:
    Status(const std::string& status_output) : status_output_(status_output) {}
    std::string generate_output() {
        char first_letter = status_output_[0];
        std::string text, class_;

        if (first_letter == 'R') {
            text = "" + status_output_.substr(1);
            class_ = "active";
        } else if (first_letter == 'P') {
            text = "" + status_output_.substr(1);
            class_ = "inactive";
        } else {
            text = "";
            class_ = "";
        }

        return "{\"text\": \"" + text + "\", \"alt\": \"Time left\", \"tooltip\": \"Time left\", \"class\": \"" + class_ + "\", \"percentage\": 100 }";
    }
};

int main(int argc, char* argv[]) {
    std::string status_output;
    if (argc > 1) {
        status_output = argv[1];
    }
    Status status(status_output);
    std::cout << status.generate_output() << std::endl;
    return 0;
}
