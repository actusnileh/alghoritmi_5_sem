import { FC, useState, CSSProperties } from "react";
import {
    Title,
    Divider,
    TextInput,
    Button,
    LoadingOverlay,
    Text,
} from "@mantine/core";
import axios from "axios";
import ReactFlow, { Controls, Background, Node, Edge } from "reactflow";
import "reactflow/dist/style.css";

// Стиль для узлов и рёбер
const nodeStyle = {
    width: 10,
    height: 10,
    borderRadius: "50%",
    backgroundColor: "#FFCC00",
    display: "flex",
    justifyContent: "center",
    alignItems: "center",
    border: "1px solid #000",
    color: "black",
    fontSize: "12px",
};

const edgeStyle: CSSProperties = {
    stroke: "#000",
    strokeWidth: 2,
    strokeLinecap: "round", // This matches the StrokeLinecap type
    strokeLinejoin: "round",
    zIndex: 2,
};

const generateNodesAndEdges = (structure: any) => {
    const nodes: Node[] = [];
    const edges: Edge[] = [];
    let nodeCounter = 0;

    // Функция для обхода дерева и вычисления позиций
    const traverseTree = (
        node: any,
        parentId: string | null = null,
        prefix: string = "",
        xOffset: number = 0,
        yOffset: number = 0
    ) => {
        const nodeId = `node-${nodeCounter++}`;
        nodes.push({
            id: nodeId,
            data: { label: "" }, // Присваиваем метку
            position: { x: xOffset, y: yOffset },
            style: nodeStyle,
        });

        if (parentId) {
            // Добавляем ребро от родителя к текущему узлу
            edges.push({
                id: `e${parentId}-${nodeId}`,
                source: parentId,
                target: nodeId,
                label: prefix, // Здесь можно использовать символ, который ведёт к текущему узлу
                style: edgeStyle,
            });
        }

        // Определяем новое смещение по X для дочерних узлов
        let childXOffset = xOffset - 100; // смещение по горизонтали для левого потомка
        const childYOffset = yOffset + 100; // смещение по вертикали для следующего уровня дерева

        // Рекурсивно добавляем переходы
        Object.keys(node.transitions).forEach((key) => {
            traverseTree(
                node.transitions[key],
                nodeId,
                prefix + key,
                childXOffset,
                childYOffset
            );
            childXOffset += 200; // Увеличиваем смещение для следующего узла на уровне
        });
    };

    // Начинаем обход с корня
    traverseTree(structure);

    return { nodes, edges };
};

export const Lab8Window: FC = () => {
    const [strings, setStrings] = useState<string>("");
    const [loading, setLoading] = useState<boolean>(false);
    const [result, setResult] = useState<any>(null);

    const handleSubmit = async () => {
        setLoading(true);
        try {
            const stringArray = strings.split(",").map((str) => str.trim());

            const response = await axios.post(
                "http://localhost:3415/v1/lab8",
                stringArray
            );

            setResult(response.data);
        } catch (error) {
            console.error("Ошибка при запросе: ", error);
        } finally {
            setLoading(false);
        }
    };

    const { nodes, edges } = result
        ? generateNodesAndEdges(result.structure)
        : { nodes: [], edges: [] };

    return (
        <div style={{ position: "relative" }}>
            <LoadingOverlay visible={loading} />
            <Title style={{ textAlign: "center" }}>
                🧩 НОП / Суффиксное дерево
            </Title>
            <Divider my="sm" />

            <TextInput
                label="Ввод строк"
                value={strings}
                onChange={(e) => setStrings(e.target.value)}
                placeholder="banana, apple, cherry"
                mb={10}
            />
            <Button onClick={handleSubmit} fullWidth>
                Решить
            </Button>
            {result && result.lcs && (
                <div style={{ marginTop: "20px", textAlign: "center" }}>
                    <Text size="lg">LCS: {result.lcs}</Text>
                </div>
            )}
            {result && (
                <div style={{ height: "500px", marginTop: "20px" }}>
                    <ReactFlow nodes={nodes} edges={edges} fitView>
                        <Controls />
                        <Background />
                    </ReactFlow>
                </div>
            )}
        </div>
    );
};
