import { Container, Title, Button, TextInput, Table } from "@mantine/core";
import { FC, useState } from "react";

interface Lab3WindowProps {
    onCalculate: (input1: string, input2: string) => Promise<void>;
    lcsData: number[][] | null;
}

export const Lab3Window: FC<Lab3WindowProps> = ({ onCalculate, lcsData }) => {
    const [input1, setInput1] = useState("");
    const [input2, setInput2] = useState("");

    return (
        <Container my="xl">
            <Title order={2} mb="xl">
                Лаб. работа №3
            </Title>
            <TextInput
                label="Первая строка"
                value={input1}
                onChange={(event) => setInput1(event.currentTarget.value)}
                mb="sm"
            />
            <TextInput
                label="Вторая строка"
                value={input2}
                onChange={(event) => setInput2(event.currentTarget.value)}
                mb="xl"
            />
            <Button size="sm" onClick={() => onCalculate(input1, input2)}>
                Посчитать
            </Button>
            {lcsData && (
                <Table mt="xl">
                    <thead>
                        <tr>
                            <th></th>
                            {input2.split("").map((char, index) => (
                                <th key={index}>{char}</th>
                            ))}
                        </tr>
                    </thead>
                    <tbody>
                        {lcsData.map((row, rowIndex) => (
                            <tr key={rowIndex}>
                                <th>
                                    {rowIndex === 0 ? "" : input1[rowIndex - 1]}
                                </th>
                                {row.map((cell, cellIndex) => (
                                    <td key={cellIndex}>{cell}</td>
                                ))}
                            </tr>
                        ))}
                    </tbody>
                </Table>
            )}
        </Container>
    );
};
