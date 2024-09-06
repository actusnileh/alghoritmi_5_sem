import {
    Button,
    Container,
    Title,
    Divider,
    Group,
    Space,
    Radio,
    RadioGroup,
    Table,
} from "@mantine/core";
import { MainWindowProps } from "../../types/lab1_types";

const exampleSortingResults = [
    {
        algorithm: "SortDirectInclusion",
        times: {
            "10 000": "1.184263",
            "100 000": "471.69584703s",
            "500 000": "6.78s",
        },
    },
    {
        algorithm: "SortDirectSelection",
        times: { "10 000": "1.556144", "100 000": "1.45s", "500 000": "7.23s" },
    },
    {
        algorithm: "SortDirectExchange",
        times: { "10 000": "4.001043", "100 000": "1.20s", "500 000": "6.50s" },
    },
    {
        algorithm: "QuickSort",
        times: {
            "10 000": "0.001278",
            "100 000": "1.628890s",
            "500 000": "25.062675s",
        },
    },
    {
        algorithm: "ShellSort",
        times: {
            "10 000": "0.010780",
            "100 000": "1.536879s",
            "500 000": "6.645918s",
        },
    },
];
export const MainWindow: React.FC<MainWindowProps> = ({
    sortingResults,
    loading,
    sortPercent,
    setSortPercent,
    fetchSortingResults,
}) => {
    return (
        <Container my="xl">
            <Title order={2} mb="xl">
                Лаб. работа №1
            </Title>
            <Divider
                my="sm"
                label="Степень отсортированности массива"
                labelPosition="center"
            />
            <RadioGroup size="md" value={sortPercent} onChange={setSortPercent}>
                <Group gap={"xl"} justify="center">
                    {["0%", "25%", "50%", "75%", "100%"].map((percent) => (
                        <Radio key={percent} value={percent} label={percent} />
                    ))}
                </Group>
            </RadioGroup>
            <Space h="xl" />
            <Divider my="sm" label="Результат" labelPosition="center" />

            <Table>
                <thead>
                    <tr>
                        <th style={{ textAlign: "center" }}>Алгоритм</th>
                        <th style={{ textAlign: "center" }}>
                            Время выполнения (сек)
                        </th>
                    </tr>
                </thead>
                <tbody>
                    {loading ? (
                        <tr>
                            <td colSpan={2} style={{ textAlign: "center" }}>
                                Загрузка...
                            </td>
                        </tr>
                    ) : sortingResults.length > 0 ? (
                        sortingResults.map((result) => (
                            <tr key={result.name}>
                                <td style={{ textAlign: "center" }}>
                                    {result.name}
                                </td>
                                <td style={{ textAlign: "center" }}>
                                    {result.time.toFixed(6)}
                                </td>
                            </tr>
                        ))
                    ) : (
                        <tr>
                            <td colSpan={2} style={{ textAlign: "center" }}>
                                Данных нет
                            </td>
                        </tr>
                    )}
                </tbody>
            </Table>

            <Group mt="lg" justify="center">
                <Button
                    radius="xl"
                    size="md"
                    onClick={fetchSortingResults}
                    disabled={loading}
                >
                    Посчитать
                </Button>
            </Group>
            <Space h="xl" />

            <Divider my="sm" label="Пример результата" labelPosition="center" />
            <Table>
                <thead>
                    <tr>
                        <th style={{ textAlign: "center" }}>Алгоритм</th>
                        <th style={{ textAlign: "center" }}>
                            10 000 элементов
                        </th>
                        <th style={{ textAlign: "center" }}>
                            100 000 элементов
                        </th>
                        <th style={{ textAlign: "center" }}>
                            500 000 элементов
                        </th>
                    </tr>
                </thead>
                <tbody>
                    {exampleSortingResults.map((result) => (
                        <tr key={result.algorithm}>
                            <td style={{ textAlign: "center" }}>
                                {result.algorithm}
                            </td>
                            <td style={{ textAlign: "center" }}>
                                {result.times["10 000"]}
                            </td>
                            <td style={{ textAlign: "center" }}>
                                {result.times["100 000"]}
                            </td>
                            <td style={{ textAlign: "center" }}>
                                {result.times["500 000"]}
                            </td>
                        </tr>
                    ))}
                </tbody>
            </Table>
        </Container>
    );
};
