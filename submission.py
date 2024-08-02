{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNHoulgLf/6s+ezt3Mcvmvd",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/blacurly/MD-ADS2024/blob/main/submission.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 3,
      "metadata": {
        "id": "HIvaBxkqgtSD",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "3c90a9cf-3cd7-4245-fe42-146fdc299c32"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "0\n"
          ]
        }
      ],
      "source": [
        "def multiply_list(number_string):\n",
        "    num_list = number_string.split()\n",
        "\n",
        "    if not num_list:\n",
        "        return 0\n",
        "\n",
        "    num_list = [int(num) for num in num_list]\n",
        "    result = 1\n",
        "\n",
        "    for num in num_list:\n",
        "        result *= num\n",
        "\n",
        "    return result\n",
        "\n",
        "input_string = \"0 1 2 1\"\n",
        "result = multiply_list(input_string)\n",
        "print(result)"
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "p3RdktNbANp8"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}