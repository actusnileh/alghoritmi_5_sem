import {
    Container,
    Divider,
    Title,
    Button,
    TextInput,
    Group,
    ActionIcon,
    Stack,
} from "@mantine/core";
import { FC, useEffect, useState } from "react";
import { IconTrash } from "@tabler/icons-react";
import { Lab2WindowProps } from "../../types/types";

export const Lab2Window: FC<Lab2WindowProps> = ({ onValuesChange }) => {
    const [inputs, setInputs] = useState([{ firstValue: "", secondValue: "" }]);

    useEffect(() => {
        if (onValuesChange) {
            const allValues = inputs.flatMap(({ firstValue, secondValue }) => [
                firstValue,
                secondValue,
            ]);
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
                <Button size="sm">Посчитать</Button>
            </Stack>
        </Container>
    );
};
