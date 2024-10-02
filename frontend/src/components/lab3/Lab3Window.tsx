import {
    Container,
    Title,
    Button,
    TextInput,
    Table,
    Text,
} from "@mantine/core";
import { FC, useState } from "react";

interface Lab3WindowProps {
    onCalculate: (input1: string, input2: string) => Promise<void>;
    lcsData: number[][] | null;
    directions: string[][] | null;
    all_lcs: string | null;
}

export const Lab3Window: FC<Lab3WindowProps> = ({
    onCalculate,
    lcsData,
    directions,
    all_lcs,
}) => {
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
                <Table
                    mt="xl"
                    striped
                    withTableBorder
                    withColumnBorders
                    highlightOnHover
                >
                    <Table.Thead>
                        <Table.Tr>
                            <Table.Th></Table.Th>
                            {input2.split("").map((char, index) => (
                                <Table.Th key={index}>{char}</Table.Th>
                            ))}
                        </Table.Tr>
                    </Table.Thead>
                    <Table.Tbody>
                        {lcsData.map((row, rowIndex) => (
                            <Table.Tr key={rowIndex}>
                                <Table.Th>
                                    {rowIndex === 0 ? "" : input1[rowIndex - 1]}
                                </Table.Th>
                                {row.map((cell, cellIndex) => (
                                    <Table.Td key={cellIndex}>{cell}</Table.Td>
                                ))}
                            </Table.Tr>
                        ))}
                    </Table.Tbody>
                </Table>
            )}
            {directions && (
                <Table
                    mt="xl"
                    striped
                    withTableBorder
                    withColumnBorders
                    highlightOnHover
                >
                    <Table.Thead>
                        <Table.Tr>
                            <Table.Th></Table.Th>
                            {input2.split("").map((char, index) => (
                                <Table.Th key={index}>{char}</Table.Th>
                            ))}
                        </Table.Tr>
                    </Table.Thead>
                    <Table.Tbody>
                        {directions.map((row, rowIndex) => (
                            <Table.Tr key={rowIndex}>
                                <Table.Th>
                                    {rowIndex === 0 ? "" : input1[rowIndex - 1]}
                                </Table.Th>
                                {row.map((cell, cellIndex) => (
                                    <Table.Td key={cellIndex}>{cell}</Table.Td>
                                ))}
                            </Table.Tr>
                        ))}
                    </Table.Tbody>
                </Table>
            )}
            <Text>{all_lcs}</Text>
        </Container>
    );
};
