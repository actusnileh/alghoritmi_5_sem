import {
    Container,
    Title,
    SegmentedControl,
    Divider,
    Stack,
    Group,
    TextInput,
    ActionIcon,
    Button,
    Image,
    Text,
} from "@mantine/core";
import { IconTrash } from "@tabler/icons-react";
import { FC, useEffect, useState } from "react";

interface Lab4WindowProps {
    onValuesChange: (values: string) => void;
}

export const Lab4Window: FC<Lab4WindowProps> = ({ onValuesChange }) => {
    const [inputs, setInputs] = useState([{ firstValue: "", secondValue: "" }]);
    const [capacity, setCapacity] = useState("");
    const [method, setMethod] = useState("Дискретный");
    const [result, setResult] = useState<any>(null);
    const [error, setError] = useState("");

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
        if (index === 0) {
            return;
        }
        setInputs(inputs.filter((_, i) => i !== index));
    };

    const handleCalculate = async () => {
        const items = inputs.map((input) => ({
            weight: parseInt(input.firstValue),
            value: parseInt(input.secondValue),
        }));

        try {
            const response = await fetch(
                `http://localhost:8000/v1/lab4?capacity=${capacity}&method=${
                    method === "Дискретный" ? "Дискретный" : "Непрерывный"
                }`,
                {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify({
                        elements: items,
                    }),
                }
            );

            if (!response.ok) {
                throw new Error("Ошибка при вычислении");
            }

            const data = await response.json();
            setResult(data);
            setError("");
        } catch (error) {
            setResult(null);
            setError("Произошла ошибка при расчете");
        }
    };

    return (
        <Container
            my="xl"
            style={{
                alignItems: "center",
                textAlign: "center",
            }}
        >
            <Title order={2} mb="xl">
                Лаб. работа №4
            </Title>

            <Divider my="sm" label="Метод" labelPosition="center" />
            <SegmentedControl
                data={["Дискретный", "Непрерывный"]}
                value={method}
                onChange={setMethod} // Обновление метода
            />

            <Divider my="sm" label="Предметы" labelPosition="center" />

            <TextInput
                placeholder="Размер рюкзака"
                value={capacity}
                onChange={(e) => setCapacity(e.target.value)}
                style={{ width: 205 }}
                mx="auto"
                mb="md"
            />

            <Stack align="center">
                {inputs.map((input, index) => (
                    <Group key={index} align="center">
                        <TextInput
                            placeholder="Вес"
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
                            style={{ width: 70 }}
                        />
                        <TextInput
                            placeholder="Цена"
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
                            style={{ width: 70 }}
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
                <Button size="sm" onClick={handleCalculate}>
                    Посчитать
                </Button>
            </Stack>

            {error && (
                <Text c="red" mt="md">
                    {error}
                </Text>
            )}

            {result && (
                <div style={{ marginTop: "20px" }}>
                    <Title order={3}>Результаты</Title>
                    <Text>Максимальная стоимость: {result.max_value}</Text>

                    {result.table && (
                        <div
                            dangerouslySetInnerHTML={{ __html: result.table }}
                            style={{
                                marginTop: "20px",
                                textAlign: "center",
                                width: "80%",
                                margin: "auto",
                            }}
                        />
                    )}

                    <div
                        style={{
                            display: "grid",
                            placeItems: "center",
                            marginTop: "20px",
                        }}
                    >
                        <Image
                            src={result.visualization}
                            alt="Visualization"
                            style={{
                                borderRadius: "30px",
                                maxWidth: "80%",
                                height: "auto",
                            }}
                        />
                    </div>
                </div>
            )}
        </Container>
    );
};
