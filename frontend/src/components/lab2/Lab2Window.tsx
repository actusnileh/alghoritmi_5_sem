import {
    Container,
    Divider,
    Title,
    Button,
    TextInput,
    Group,
    ActionIcon,
    Stack,
    Table,
    Text,
    Center,
} from "@mantine/core";
import { FC, useEffect, useState } from "react";
import { IconTrash } from "@tabler/icons-react";

interface Lab2WindowProps {
    onValuesChange: (values: string) => void;
    onCalculate: () => void;
    matrixData?: {
        matrix: number[][];
        k: number[][];
        optimal_brackets: string;
    };
}

export const Lab2Window: FC<Lab2WindowProps> = ({
    onValuesChange,
    onCalculate,
    matrixData,
}) => {
    const [inputs, setInputs] = useState([{ firstValue: "", secondValue: "" }]);

    useEffect(() => {
        if (onValuesChange) {
            const allValues = inputs.flatMap(({ firstValue, secondValue }) =>
                secondValue ? [firstValue, secondValue] : [firstValue]
            );
            const valuesString = allValues.join(",");
            onValuesChange(valuesString);
        }
    }, [inputs, onValuesChange]);

    const addInputPair = () => {
        setInputs([...inputs, { firstValue: "", secondValue: "" }]);
    };

    const removeInputPair = (index: number) => {
        setInputs(inputs.filter((_, i) => i !== index));
    };

    const renderMatrix = (matrix: number[][]) => {
        return (
            <div style={{ margin: "20px", textAlign: "center" }}>
                <Table
                    striped
                    withColumnBorders
                    highlightOnHover
                    captionSide="top"
                    verticalSpacing="sm"
                    horizontalSpacing="md"
                    style={{ margin: "0 auto" }}
                >
                    <thead>
                        <tr>
                            {matrix[0]?.map((_, index) => (
                                <th key={index} style={{ textAlign: "center" }}>
                                    {index + 1}
                                </th>
                            ))}
                        </tr>
                    </thead>
                    <tbody>
                        {matrix.map((row, rowIndex) => (
                            <tr key={rowIndex}>
                                {row.map((cell, cellIndex) => (
                                    <td
                                        key={cellIndex}
                                        style={{
                                            textAlign: "center",
                                            padding: "8px",
                                            border: "1px solid #ccc",
                                        }}
                                    >
                                        {cell}
                                    </td>
                                ))}
                            </tr>
                        ))}
                    </tbody>
                </Table>
            </div>
        );
    };

    return (
        <Container my="xl">
            <Title order={2} mb="xl">
                Лаб. работа №2
            </Title>
            <Divider
                my="sm"
                label="Список размеров матриц"
                labelPosition="center"
            />
            <Stack align="center">
                {inputs.map((input, index) => (
                    <Group key={index} align="center">
                        <TextInput
                            placeholder="10"
                            value={input.firstValue}
                            onChange={(e) =>
                                setInputs(
                                    inputs.map((inp, i) =>
                                        i === index
                                            ? {
                                                  ...inp,
                                                  firstValue: e.target.value,
                                              }
                                            : inp
                                    )
                                )
                            }
                            style={{ width: 50 }}
                        />
                        <TextInput
                            placeholder="15"
                            value={input.secondValue}
                            onChange={(e) =>
                                setInputs(
                                    inputs.map((inp, i) =>
                                        i === index
                                            ? {
                                                  ...inp,
                                                  secondValue: e.target.value,
                                              }
                                            : inp
                                    )
                                )
                            }
                            style={{ width: 50 }}
                        />
                        <ActionIcon
                            color="red"
                            size={"lg"}
                            onClick={() => removeInputPair(index)}
                        >
                            <IconTrash size={18} />
                        </ActionIcon>
                    </Group>
                ))}
                <Button size="sm" onClick={addInputPair}>
                    +
                </Button>
                <Button onClick={onCalculate} size="sm">
                    Посчитать
                </Button>
            </Stack>
            {matrixData && (
                <Container mt="xl">
                    <Center>
                        <Title order={4}>Matrix</Title>
                    </Center>
                    {renderMatrix(matrixData.matrix)}

                    {/* <Center mt="xl"> */}
                    {/* <Title order={4}>K</Title> */}
                    {/* </Center> */}
                    {/* {renderMatrix(matrixData.k)} */}

                    <Center mt="xl">
                        <Text size="lg">{matrixData.optimal_brackets}</Text>
                    </Center>
                </Container>
            )}
        </Container>
    );
};
