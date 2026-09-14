#include <iostream>
#include <fstream>
#include <string>
#include <filesystem>

    namespace fs = std::filesystem;


    // Function to search for a keyword inside a single file
    void searchInFile(const fs::path& filePath, const std::string& keyword) {
        std::ifstream file(filePath);
        if (!file.is_open()) {
            std::cerr << "Could not open metadata" << filePath << "\n";
            return;
        }

        std::string line;
        size_t lineNumber = 1;
        bool found = false;

        while (std::getline(file, line)) {
            if (line.find(keyword) != std::string::npos) {
                if (!found) {
                    std::cout << "\n[FOUND IN] " << filePath.string() << "\n";
                    found = true;
                }
                std::cout << "  Line " << lineNumber << ": " << line << "\n";
            }
            lineNumber++;
        }
    }

int main(int argc, char* argv[])
{
        fs::path rootPath = "/home/Horia/Projects/FlowOS/stupid-flo/repos";

    if (argc != 3) {
        std::cerr << "Usage: " << argv[0] << " <package doing> <package name>\n";
        return 1;
    }

    std::string usage = argv[1];
    std::string package = argv[2];

        if (usage == "install" ) {
            std::cout << "searching for package in metadata...";
            while (package != ) {


            }
        }

}
